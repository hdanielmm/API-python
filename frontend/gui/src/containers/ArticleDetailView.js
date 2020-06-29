import React from 'react';
import axios from 'axios';
import { Card } from 'antd';


class ArticleDetail extends React.Component {

  state = {
    article: {}
  }

  componentDidMount () {
    const articleID = this.props.match.params.articleID;
    axios.get(`http://127.0.0.1:8000/api/${articleID}`)
      .then(res => {
        this.setState({
          article: res.data
        });
        console.log("res.data", res.data);
      })
      .catch(err => {
        console.log(err);
      })
  }

  render () {
    return (
      <Card title={this.state.article.brand}>
        <p>{this.state.article.nationality}</p>
        <p>{this.state.article.alcohol}% vol</p>
        <p>{this.state.article.milliliters}ml</p>
      </Card>
    )
  }
}

export default ArticleDetail;