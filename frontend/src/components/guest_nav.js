import React from 'react';

import Logo from './logo'

import './guest_nav.scss';

class GuestNav extends React.Component {
  render() {
    return (
      <div className='guest-nav'>
        <Logo />
      </div>
    );
  }
}

export default GuestNav;
