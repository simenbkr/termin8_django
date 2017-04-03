import React, { Component } from 'react'
import ListItem from '../ListItem'


class List extends Component {

    state = {
        articles: []
    };

    async loadArticles() {
        this.setState({
            articles: await fetch('/api/articles/')
                .then(response =>response.json())
        })
    }

    componentDidMount() {
        // if DOM was rendered
        this.loadArticles();
    }

    render(){
        // fake delays
        setTimeout(() => {this.setState({timePassed: true})}, 500)

        if (!this.state.timePassed){
            // loading page
            return <div>Loading...</div>;
        }
        else {
            return(
                <ul className="content_list">
                    { this.state.articles.map((article, index) => (
                        <li className="list_item" key={ index }>
                            <ListItem article={ article } />
                        </li>
                    ))}
                </ul>
            );
        }
    }
}


export default List
