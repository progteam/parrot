import React from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

import './about_officers.scss';

const Officer = ({
  email,
  name,
  profileImg,
  role,
}) => (
  <div className="officer">
    <img
      src={profileImg}
      alt={`${name}`}
      className="profile-img"
    />
    <div className="name">{name}</div>
    <div className="role">{role}</div>
    <div className="email">{email}</div>
  </div>
);

Officer.propTypes = {
  email: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  profileImg: PropTypes.string.isRequired,
  role: PropTypes.string.isRequired,
};

class Officers extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      officers: [],
    };
  }

  componentDidMount() {
    this.getOfficers();
  }

  async getOfficers() {
    const res = await axios.get('/about/officer-info');
    const { data } = res;
    this.setState({
      officers: data,
    });
  }

  render() {
    const { officers } = this.state;
    // Avoid destructuring assignment here since we want to spread the args
    /* eslint-disable react/destructuring-assignment */
    return (
      <div className="officers">
        {officers.map(officer => (
          <Officer
            key={officer.name}
            {...officer}
          />
        ))}
      </div>
    );
  }
}

export default Officers;
