import { hot } from 'react-hot-loader';
import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { withStyles } from '@material-ui/core/styles';
import { lowerCase } from 'change-case';
import resolve from 'resolve-pathname';
import catchLinks from 'catch-links';
import 'prismjs';
import 'prismjs/themes/prism.css';
import 'prism-themes/themes/prism-atom-dark.css';
import 'prismjs/components/prism-javascript';
import 'prismjs/components/prism-json';
import 'prismjs/components/prism-yaml';
import 'prismjs/components/prism-markup';
import Dashboard from '../../components/Dashboard';
import HeaderWithAnchor from '../../components/HeaderWithAnchor';
import NotFound from '../../components/NotFound';
import ScrollToTop from '../../utils/ScrollToTop';
import { DOCS_PATH_PREFIX, DOCS_MENU_ITEMS } from '../../utils/constants';
import scrollToHash from '../../utils/scrollToHash';
import readDocFile from '../../utils/readDocFile';
import removeReadmeFromPath from '../../utils/removeReadmeFromPath';
import docsTableOfContents from '../../autogenerated/docs-table-of-contents';
import PageMeta from './PageMeta';

@hot(module)
@withStyles(
  theme => ({
    innerHtml: {
      ...theme.mixins.markdown,
      '& .token.operator': {
        color: 'none',
        background: 'none',
      },
    },
  }),
  { withTheme: true }
)
export default class Documentation extends Component {
  state = {
    error: null,
    Page: null,
    pageInfo: null,
  };

  componentDidMount() {
    this.load();

    window.addEventListener('load', this.handleDomLoad);
  }

  componentWillUnmount() {
    window.removeEventListener('load', this.handleDomLoad);
  }

  handleDomLoad = () => {
    const { theme, history } = this.props;

    // Clicking a link from markdown opens a new page.
    // We need to make sure react-router is still used for local routes.
    // Note: The callback will only be triggered for relative links
    catchLinks(window, href => {
      history.push(href);

      scrollToHash(theme.spacing.double);
    });

    // Handle initial scroll if necessary
    if (this.props.history.location.hash) {
      scrollToHash(theme.spacing.double);
    }
  };

  componentDidUpdate(prevProps) {
    if (this.props.match.params.path === prevProps.match.params.path) {
      return;
    }

    this.load();
  }

  anchorFactory = ({ href, children, ...props }) => {
    if (href.startsWith('http')) {
      return (
        <a href={href} {...props} target="_blank" rel="noopener noreferrer">
          {children}
        </a>
      );
    }

    const { location } = this.props;
    const url = resolve(href, location.pathname);

    return (
      <Link to={url} {...props}>
        {children}
      </Link>
    );
  };

  headingFactory = type => ({ children, id, ...props }) => (
    <HeaderWithAnchor type={type} id={id} {...props}>
      {children}
    </HeaderWithAnchor>
  );

  findChildFromRootNode(node) {
    const currentPath = window.location.pathname.replace(
      `${DOCS_PATH_PREFIX}/`,
      ''
    );

    if (node.path && currentPath === removeReadmeFromPath(node.path)) {
      return node;
    }

    if (node.children) {
      for (let i = 0; i < node.children.length; i += 1) {
        const result = this.findChildFromRootNode(node.children[i]);

        if (result) {
          return result;
        }
      }
    }
  }

  getPageInfo() {
    const menuItem = DOCS_MENU_ITEMS.find(
      ({ path }) =>
        window.location.pathname !== DOCS_PATH_PREFIX &&
        path !== DOCS_PATH_PREFIX &&
        window.location.pathname.startsWith(path)
    );

    if (!menuItem) {
      return null;
    }

    const rootNode = docsTableOfContents[lowerCase(menuItem.label)];

    return this.findChildFromRootNode(rootNode);
  }

  // Returns a mapping between the HTML element and the desired component
  components() {
    return {
      a: this.anchorFactory,
      h1: this.headingFactory('h1'),
      h2: this.headingFactory('h2'),
      h3: this.headingFactory('h3'),
      h4: this.headingFactory('h4'),
      h5: this.headingFactory('h5'),
      h6: this.headingFactory('h6'),
    };
  }

  async load() {
    try {
      const { params } = this.props.match;
      const pathname = params.path || 'README';
      const { loader } = readDocFile(`${pathname}.md`);
      const { default: Page } = await loader;
      const pageInfo = this.getPageInfo();

      this.setState({ Page, pageInfo, error: null });
    } catch (error) {
      this.setState({ error });
    }
  }

  render() {
    const { classes, history } = this.props;
    const { error, Page, pageInfo } = this.state;

    return (
      <Dashboard
        className={classes.innerHtml}
        docs
        title={
          pageInfo && pageInfo.data.title
            ? pageInfo.data.title
            : 'Documentation'
        }>
        <ScrollToTop>
          {error ? (
            <NotFound isDocs />
          ) : (
            Page && <Page components={this.components()} />
          )}
          {pageInfo && <PageMeta pageInfo={pageInfo} history={history} />}
        </ScrollToTop>
      </Dashboard>
    );
  }
}
