import React from 'react';
import GuestNav from '../components/guest_nav';
import LandingFooter from '../landing/landing_footer';
import SubKatHandle from '../components/subscribe_kattis_handle';
import ScoreBoardDelta from '../components/scoreboard_delta';

import './scoreboard.scss';

const ScoreBoard = () => (
  <div className="scoreboard">
    <GuestNav />

    <div className="main">
      <div className="padding-around" />
      <SubKatHandle />
      <div className="padding-around" />
      <ScoreBoardDelta />
      <div className="padding-around" />
    </div>

    <LandingFooter />
  </div>
);


export default ScoreBoard;
