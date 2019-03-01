import React from 'react';
import ReactSVG from 'react-svg';

import './logo.scss';

const Logo = () => (
  /*
   * We use React-SVG to load the logo from %PUBLIC_URL%.
   *  https://www.npmjs.com/package/react-svg
   */
  <ReactSVG
    fallback="MBPT"
    src={`${process.env.PUBLIC_URL}/logo.svg`}
    svgClassName="logo"
  />
);

export default Logo;
