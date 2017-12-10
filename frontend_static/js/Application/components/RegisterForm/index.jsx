import React from 'react';
import {Form, Button, Input, Icon, Row, Col} from 'antd';
import autobind from 'autobind-decorator';

import ApiRequest from '../../../_common/ApiRequest';


export class RegisterForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password1: '',
      password2: '',
    };
  }

  @autobind
  onUserNameChange(e) {
    this.setState({
      username: e.target.value,
    });
  }

  @autobind
  onPassword1Change(e) {
    this.setState({
      password1: e.target.value,
    });
  }

  @autobind
  onPassword2Change(e) {
    this.setState({
      password2: e.target.value,
    });
  }

  @autobind
  onSubmit(e) {
    e.preventDefault();
    const data = {
      username: this.state.username,
      password: this.state.password1,
    };
    ApiRequest.post('/user/register', data)
      .then(() => window.location = '/')
      .catch(() => console.log('error'));
  }

  render() {
    return (
      <div style={{textAlign: 'center', paddingTop: '10em'}}>
        <Form onSubmit={this.onSubmit}>
          <h1>Register</h1>
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
                value={this.state.password1}
                onChange={this.onPassword1Change}
                type="password"
              />
            </Col>
          </Row>
          <Row style={{padding: '1em'}}>
            <Col span={6} offset={9}>
              <Input
                placeholder="Repeat your password"
                prefix={<Icon type="lock" style={{color: 'rgba(0,0,0,.25)'}}/>}
                value={this.state.password2}
                onChange={this.onPassword2Change}
                type="password"
              />
            </Col>
          </Row>
          <Row style={{padding: '1em'}}>
            <Col span={6} offset={9}>
              <Button type="primary" htmlType="submit">Register</Button>
            </Col>
          </Row>
        </Form>
      </div>
    )
  }
}
