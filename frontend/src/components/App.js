import React, { Component } from 'react';
import { render } from 'react-dom';
import ReactDOM from 'react-dom';

class App extends Component {
  render() {
    return (
        <h1>Hola Orlando</h1>
    )
  }      
}

ReactDOM.render(<App />, document.getElementById('app'));