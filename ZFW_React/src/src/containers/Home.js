import React, { Component } from 'react';
import { Container , Jumbotron } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../css/main.css';

export default class Home extends Component {
    constructor(props) {
        super(props);
        this.state = {};
    }
    render() {
        return (
                <Jumbotron as="section" className="text-center">
                    <Container>
                        <h1>数智教育</h1>
                        <p className="lead text-muted">这是基本介绍</p>
                    </Container>
                </Jumbotron>
                /* <div className="album">
                    <div className="row">
                        <div className="col-xl">
                            <Card className="mb-4 box-shadow">
                                <Card.Img variant="top" src={uestc} style={{width: "256px", height: "256px"}}/>
                                <Card.Body>
                                    <Card.Title>学校层面</Card.Title>
                                    <Card.Text>学校层面介绍</Card.Text>
                                </Card.Body>
                            </Card>
                        </div>
                        <div className="col-xl">
                            <Card className="mb-4 box-shadow">
                                <Card.Img variant="top" src={uestc} style={{width: "256px", height: "256px"}}/>
                                <Card.Body>
                                    <Card.Title>班级层面</Card.Title>
                                    <Card.Text>班级层面介绍</Card.Text>
                                </Card.Body>
                            </Card>
                        </div>
                        <div className="col-xl">
                            <Card className="mb-4 box-shadow">
                                <Card.Img variant="top" src={uestc} style={{width: "256px", height: "256px"}}/>
                                <Card.Body>
                                    <Card.Title>学生层面</Card.Title>
                                    <Card.Text>学生层面介绍</Card.Text>
                                </Card.Body>
                            </Card>
                        </div>
                        <div className="col-xl">
                            <Card className="mb-4 box-shadow">
                                <Card.Img variant="top" src={uestc} style={{width: "256px", height: "256px"}}/>
                                <Card.Body>
                                    <Card.Title>应用层面</Card.Title>
                                    <Card.Text>应用层面介绍</Card.Text>
                                </Card.Body>
                            </Card>
                        </div>
                    </div>
                </div> */
        );
    }
}
