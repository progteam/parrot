import React from 'react';

import './landing_footer.scss';

const FooterLink = (props) => {
  return (
    <a
      target='_blank'
      rel='noopener noreferrer'
      href={props.href}>
      {props.children}
    </a>
  );
};

const LandingFooter = (props) => {
  return (
    <div className='landing-footer'>
      <FooterLink href='https://csumb.edu/'>
        CSUMB
      </FooterLink>
      <FooterLink href='https://github.com/progteam'>
        GitHub
      </FooterLink>
      <FooterLink href='https://open.kattis.com/universities/csumb.edu'>
        Kattis
      </FooterLink>
    </div>
  );
};

export default LandingFooter;
