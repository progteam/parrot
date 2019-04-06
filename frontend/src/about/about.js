import React from 'react';

import GuestNav from '../components/guest_nav';
import Meetings from './about_meetings';
import Officers from './about_officers';
import Overview from './about_overview';

import './about.scss';


const AboutPage = () => (
  <div className="about">
    <GuestNav />
    <div className="main">
      <div className="left-panel">
        <Overview />
      </div>
      <div className="right-panel">
        <Officers />
        <Meetings />
      </div>
    </div>
  </div>
);

export default AboutPage;
