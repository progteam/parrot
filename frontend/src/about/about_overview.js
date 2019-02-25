import React from 'react';
import axios from 'axios';
import assert from 'assert';

import './about_overview.scss';

class Overview extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      desc: '',
    };
  }

  componentDidMount() {
    this.getDesc();
  }

  async getDesc() {
    let desc;
    try {
      const res = await axios.get('/about/progteam-desc');
      ({ data: { desc } } = res);
      /*
       * We assert the returned description from the backend is a string. Or we
       * will render the error message.
       */
      assert(typeof desc === 'string');
    } catch (err) {
      desc = '<p>Sorry, something\'s wrong. Try again, maybe?</p>';
    }

    /*
     * The type of desc is an object from eslint's perspective. However, it is,
     * in fact, a string.
     */

    /* eslint-disable object-shorthand */
    this.setState({
      desc: desc,
    });
    /* eslint-enable object-shorthand */
  }

  render() {
    /*
     * The admins should have the privilege to update the content of this
     * component, as HTML. Thus, we disable the lint warning here.
     */

    const { desc } = this.state;
    /* eslint-disable react/no-danger */
    return (
      <div
        className="overview"
        dangerouslySetInnerHTML={{ __html: desc }}
      />
    );
  }
}

export default Overview;
