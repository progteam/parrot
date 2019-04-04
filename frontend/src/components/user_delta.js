import React from 'react';
import PropTypes from 'prop-types';

import './user_delta.scss';

const UserDelta = ({ delta, maxDelta, name }) => {
  const percentWidth = delta / maxDelta;

  const onDemandResize = {
    width: 100 * percentWidth,
  };
  onDemandResize.width += '%';

  const classes = `user_delta  ${percentWidth === 0 ? 'zero_delta' : ''}`;

  return (
    <div className="user_bar">
      <div className="user_name">
        <strong>
          {name}
        </strong>
      </div>
      <div className={classes} style={onDemandResize}>
        {delta}
      </div>
    </div>
  );
};

UserDelta.propTypes = {
  delta: PropTypes.number.isRequired,
  maxDelta: PropTypes.number.isRequired,
  name: PropTypes.string.isRequired,
};

export default UserDelta;
