import React from 'react';
import PropTypes from 'prop-types';

import GuestNav from '../components/guest_nav';

import './page404.scss';

const Page404 = ({ location }) => (
  <div className="page-404">
    <GuestNav />
    <div className="main">
      <p>
        Oops! We couldn
        {'\''}
        t find page
        <code>
          {location.pathname}
        </code>
      </p>
    </div>
  </div>
);

Page404.propTypes = {
  location: PropTypes.shape({
    pathname: PropTypes.string.isRequired,
  }).isRequired,
};

export default Page404;
