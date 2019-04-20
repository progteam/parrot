import React from 'react';

import './subscribe_kattis_handle.scss';

class SubKatHandle extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      kattisHandle: '',
    };

    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    this.setState({ kattisHandle: event.target.value });
  }

  render() {
    const {
      kattisHandle,
    } = this.state;

    return (
      <div className="form">

        <label htmlFor="kattisHandleBox">
          <strong> Subscribe to the graph! </strong>
          <input name="kattisHandleBox" type="text" value={kattisHandle} placeholder=" Kattis Handle" onChange={this.handleChange} />
        </label>

        <button type="button"> Subscribe </button>

      </div>
    );
  }
}

export default SubKatHandle;
