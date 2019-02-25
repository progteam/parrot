import React from 'react';

import GuestNav from '../components/guest_nav';
import LandingFooter from './landing_footer';

import './landing.scss';

const LandingPage = (props) => {
  return (
    <div className='landing'>
      <GuestNav />
      <div className='main'>
        <p>
          We choose to be
          <strong>better</strong>
        </p>
      </div>
      <LandingFooter />
    </div>
  );
};

export default LandingPage;
