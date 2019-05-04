import React from 'react';
import { Card, ListGroup, Row, Col } from 'react-bootstrap';
import studentInfo from '../data/student/Student_Info_1.json'

function List(){

    return (
        <ListGroup>
            {/* <ListGroup.Item>学生个人信息</ListGroup.Item> */}
            <ListGroup.Item variant="success" style={{height: '42px'}}>
                <Row>
                    <Col className='studentInfo_title'>学生姓名：</Col>
                    <Col md="auto">{studentInfo.info[0]}</Col>
                </Row>
            </ListGroup.Item>
            <ListGroup.Item style={{height: '42px'}}>
                <Row>
                    <Col className='studentInfo_title'>学生学号：</Col>
                    <Col md="auto">{studentInfo.info[1]}</Col>
                </Row>
            </ListGroup.Item>
            <ListGroup.Item variant="success" style={{height: '42px'}}>
                <Row>
                    <Col className='studentInfo_title'>学生性别：</Col>
                    <Col md="auto">{studentInfo.info[2]}</Col>
                </Row>
            </ListGroup.Item>
            <ListGroup.Item style={{height: '42px'}}>
                <Row>
                    <Col className='studentInfo_title'>民族：</Col>
                    <Col md="auto">{studentInfo.info[3]}</Col>
                </Row>
            </ListGroup.Item>
            <ListGroup.Item variant="success" style={{height: '42px'}}>
                <Row>
                    <Col className='studentInfo_title'>班级：</Col>
                    <Col md="auto">{studentInfo.info[4]}</Col>
                </Row>
            </ListGroup.Item>
            <ListGroup.Item style={{height: '42px'}}>
                <Row>
                    <Col className='studentInfo_title'>出生日期：</Col>
                    <Col md="auto">{studentInfo.info[5]}</Col>
                </Row>
            </ListGroup.Item>
            <ListGroup.Item variant="success" style={{height: '42px'}}>
                <Row>
                    <Col className='studentInfo_title'>籍贯：</Col>
                    <Col md="auto">{studentInfo.info[6]}</Col>
                </Row>
            </ListGroup.Item>
            <ListGroup.Item style={{height: '42px'}}>
                <Row>
                    <Col className='studentInfo_title'>政治面貌：</Col>
                    <Col md="auto">{studentInfo.info[7]}</Col>
                </Row>
            </ListGroup.Item>
            <ListGroup.Item variant="success" style={{height: '42px'}}>
                <Row>
                    <Col className='studentInfo_title'>住宿信息：</Col>
                    <Col md="auto">{studentInfo.info[8]}</Col>
                </Row>
            </ListGroup.Item>
            <ListGroup.Item style={{height: '42px'}}>
                <Row>
                    <Col className='studentInfo_title'>寝室号：</Col>
                    <Col md="auto">{studentInfo.info[9]}</Col>
                </Row>
            </ListGroup.Item>
            <ListGroup.Item variant="success" style={{height: '42px'}}>
                <Row>
                    <Col className='studentInfo_title'>寝室人数：</Col>
                    <Col md="auto">{studentInfo.info[10]}</Col>
                </Row>
            </ListGroup.Item>
        </ListGroup>
    )
}

export default function(){
    return (
        <Card>
            <Card.Header>
                <h4>学生个人信息</h4>
            </Card.Header>
            <Card.Body>
                <div style={{height: '450px'}}>
                    <List/>
                </div>
            </Card.Body>
        </Card>
    )
}