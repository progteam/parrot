import React from 'react';
import GuestNav from '../components/guest_nav';
import LandingFooter from '../landing/landing_footer';
import ScoreBoardDelta from './scoreboard_delta';

import './scoreboard.scss';

const ScoreBoard = () => (
  <div className="scoreboard">
    <GuestNav />

    <div className="main">
      <ScoreBoardDelta />
    </div>

    <LandingFooter />
  </div>
);


export default ScoreBoard;
