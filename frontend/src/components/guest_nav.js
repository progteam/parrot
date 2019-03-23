import React from 'react';
import { NavLink } from 'react-router-dom';

import Logo from './logo';

import './guest_nav.scss';

const GuestNav = () => (
  <div className="guest-nav">
    <Logo />
    <div className="links">
      <NavLink to="/about" activeClassName="active">About</NavLink>
      <NavLink to="/events" activeClassName="active">Events</NavLink>
    </div>
  </div>
);

export default GuestNav;
