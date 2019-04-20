import React from 'react';
import GuestNav from '../components/guest_nav';
import LandingFooter from '../landing/landing_footer';
import ScoreboardDelta from './scoreboard_delta';

import './scoreboard.scss';

const ScoreboardPage = () => (
  <div className="scoreboard">
    <GuestNav />

    <div className="main">
      <ScoreboardDelta />
    </div>

    <LandingFooter />
  </div>
);


export default ScoreboardPage;
