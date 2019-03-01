import React from 'react';
import PropTypes from 'prop-types';

import './landing_footer.scss';

const FooterLink = ({ href, children }) => (
  <a
    target="_blank"
    rel="noopener noreferrer"
    href={href}
  >
    {children}
  </a>
);

FooterLink.propTypes = {
  href: PropTypes.string.isRequired,
  children: PropTypes.string.isRequired,
};

const LandingFooter = () => (
  <div className="landing-footer">
    <FooterLink href="https://csumb.edu/">
      CSUMB
    </FooterLink>
    <FooterLink href="https://github.com/progteam">
      GitHub
    </FooterLink>
    <FooterLink href="https://open.kattis.com/universities/csumb.edu">
      Kattis
    </FooterLink>
  </div>
);

export default LandingFooter;
