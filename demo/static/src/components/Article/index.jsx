import React, { Component } from 'react'
import { Link } from 'react-router'

class Article extends Component {
    state = {
        title: '',
        created_at: '',
        text: ''
    };

    loadArticle(article_id) {
        fetch(`/api/articles/${article_id}/`)
            .then(response => response.json())
            .then(data => {
                this.setState(data)
            });
    }

    componentDidMount() {
        this.loadArticle(this.props.params['article_id']);
    }

    render(){

        const { title, created_at, text } = this.state;
        return(
            <div className="article">
                <h4 className="article_title">{ title }</h4>
                <small className="article_time">
                    { new Date(created_at).toDateString() }
                </small>
                <article className="article_text" dangerouslySetInnerHTML={ {__html: text} } />

                <Link className="article_button" to="/">All articles</Link>
            </div>
        );
    }

}


export default Article
