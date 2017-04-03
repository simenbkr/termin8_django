import React from 'react'
import ReactDOM from 'react-dom'

import { App } from './components'


ReactDOM.render(
    <App />,
    document.getElementById("app")
);

/* Issue with reloading page:
http://stackoverflow.com/questions/27928372/react-router-urls-dont-work-when-refreshing-or-writting-manually
*/
