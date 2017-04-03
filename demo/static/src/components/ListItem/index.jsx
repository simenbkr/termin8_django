import React, { Component } from 'react'
import { Link } from 'react-router'


class ListItem extends Component {
    render (){
        let article = this.props.article;
        let article_date = new Date(this.props.article['created_at']).toDateString();

        return(
            <div>
                <h4>
                    <Link to={`/${ article.id }`}>{ article.title }</Link>
                </h4>
                <small className="time">{ article_date }</small>

                <article dangerouslySetInnerHTML={{__html: article['announce']}} />
            </div>
        )
    };
}

export default ListItem
