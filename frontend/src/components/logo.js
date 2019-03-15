import React from 'react';
import { Link } from 'react-router-dom';
import ReactSVG from 'react-svg';

import './logo.scss';

const Logo = () => (
  /*
   * We use React-SVG to load the logo from %PUBLIC_URL%.
   *  https://www.npmjs.com/package/react-svg
   */
  <Link to="/" className="logo">
    <ReactSVG
      fallback="MBPT"
      src={`${process.env.PUBLIC_URL}/logo.svg`}
      svgClassName="logo-svg"
    />
  </Link>
);

export default Logo;
