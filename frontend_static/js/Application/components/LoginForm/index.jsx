import React from 'react';
import {Form, Button, Input, Icon, Row, Col} from 'antd';
import autobind from 'autobind-decorator';


export class LoginForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: '',
    };
  }

  @autobind
  onUserNameChange(e) {
    this.setState({
      username: e.target.value,
    });
  }

  @autobind
  onPasswordChange(e) {
    this.setState({
      password: e.target.value,
    });
  }

  @autobind
  onSubmit(e) {
    e.preventDefault();
    console.log('submit');
  }

  render() {
    return (
      <div style={{textAlign: 'center', paddingTop: '10em'}}>
        <Form onSubmit={this.onSubmit}>
          <h1>Login</h1>
          <Row style={{padding: '1em'}}>
            <Col span={6} offset={9}>
              <Input
                placeholder="Enter your username"
                value={this.state.username}
                onChange={this.onUserNameChange}
                prefix={<Icon type="user" style={{color: 'rgba(0,0,0,.25)'}}/>}
              />
            </Col>
          </Row>
          <Row style={{padding: '1em'}}>
            <Col span={6} offset={9}>
              <Input
                placeholder="Enter your password"
                prefix={<Icon type="lock" style={{color: 'rgba(0,0,0,.25)'}}/>}
                value={this.state.password}
                onChange={this.onPasswordChange}
                type="password"
              />
            </Col>
          </Row>
          <Row style={{padding: '1em'}}>
            <Col span={6} offset={9}>
              <Button type="primary" htmlType="submit">Login</Button>
            </Col>
          </Row>
        </Form>
      </div>
    )
  }
}
