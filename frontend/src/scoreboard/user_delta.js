import React from 'react';
import PropTypes from 'prop-types';

import './user_delta.scss';

const UserDelta = ({ points, maxDelta, username }) => {
  const percentWidth = points / (maxDelta + 3);

  const onDemandResize = {
    width: 100 * percentWidth + 2.5,
  };
  onDemandResize.width += '%';

  const classes = `user-delta  ${percentWidth === 0 ? 'zero-delta' : ''}`;

  return (
    <div className="user-bar">
      <div className="user-name">
        <strong>
          {username}
        </strong>
      </div>
      <div className={classes} style={onDemandResize}>
        {points.toFixed(1)}
      </div>
    </div>
  );
};

UserDelta.propTypes = {
  points: PropTypes.number.isRequired,
  maxDelta: PropTypes.number.isRequired,
  username: PropTypes.string.isRequired,
};

export default UserDelta;
