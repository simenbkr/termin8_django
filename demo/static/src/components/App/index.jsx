import React, { Component } from 'react'
import { Router, Route, IndexRoute, Link, hashHistory } from 'react-router'

import List from '../List'
import Article from '../Article'


class App extends Component {
    render(){
        return(
            <Router history={ hashHistory }>
                <Route path="/">
                    <IndexRoute component={ List } />
                    <Route path="/:article_id" component={ Article } />
                </Route>
            </Router>
        );
    }
}


export default App
