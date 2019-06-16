import React from 'react';
import { Container , Jumbotron , Card } from 'react-bootstrap';
import jpgSchScore from '../img/school_score.jpg';
import jpgClass from '../img/class.jpg';
import jpgStudent from '../img/student.jpg';
import jpgApp from '../img/app.jpg';

export default class extends React.Component {
    render() {
        return (
            <div className='overflow-y-hidden'>
                <Jumbotron as="section" className="text-center">
                    <Container>
                        <h1 className='mb-4'>数智教育</h1>
                        <p className="lead text-muted">设计思路：从整体到局部，从分析到<strong>应用</strong>，针对不同人群</p>
                        <p className="lead text-muted">面向人群：<strong>校领导层</strong>、<strong>班主任</strong>、<strong>科任教师</strong>、<strong>家长</strong>、<strong>学生</strong></p>
                        <p className="lead text-muted">组件介绍：对于部分组件，提供组件<span className='badge badge-info'>说明</span>，详细介绍组件的<strong>设计理念</strong>和<strong>功能</strong></p>
                    </Container>
                </Jumbotron>
                <div className='row mb-4'>
                    <div className='col-12 col-lg-3'>
                        <Card>
                            <Card.Img variant="top" src={jpgSchScore} />
                            <Card.Body>
                                <Card.Title>学校层面</Card.Title>
                                <Card.Text>主要面向人群: 校领导层</Card.Text>
                                <Card.Text>次要面向人群: 班主任、科任教师</Card.Text>
                                <hr />
                                <Card.Text>主要功能: 以整个学校为研究对象，全面研究校全体学生各项数据指标</Card.Text>
                                <hr />
                                <Card.Text>亮点: 班级多角度对比、高峰预警</Card.Text>
                            </Card.Body>
                        </Card>
                    </div>
                    <div className='col-12 col-lg-3'>
                        <Card>
                            <Card.Img variant="top" src={jpgClass} />
                            <Card.Body>
                                <Card.Title>班级层面</Card.Title>
                                <Card.Text className='mb-1'>主要面向人群: 班主任、科任教师</Card.Text>
                                <Card.Text className='mb-1'>次要面向人群: 校领导层、家长、学生</Card.Text>
                                <hr />
                                <Card.Text>主要功能: 选取代表性班级，具体分析班级的数据指标</Card.Text>
                                <hr />
                                <Card.Text>亮点: 班级帮扶</Card.Text>
                            </Card.Body>
                        </Card>
                    </div>
                    <div className='col-12 col-lg-3'>
                        <Card>
                            <Card.Img variant="top" src={jpgStudent} />
                            <Card.Body>
                                <Card.Title>学生层面</Card.Title>
                                <Card.Text className='mb-1'>主要面向人群: 班主任、家长、学生</Card.Text>
                                <Card.Text className='mb-1'>次要面向人群: 校领导层、科任教师</Card.Text>
                                <hr />
                                <Card.Text>主要功能: 选取代表性学生，详细描述学生各方面信息</Card.Text>
                                <hr />
                                <Card.Text>亮点: 成绩预测、排名置信区间</Card.Text>
                            </Card.Body>
                        </Card>
                    </div>
                    <div className='col-12 col-lg-3'>
                        <Card>
                            <Card.Img variant="top" src={jpgApp} />
                            <Card.Body>
                                <Card.Title>应用层面</Card.Title>
                                <Card.Text className='mb-1'>面向人群: 所有人群</Card.Text>
                                <hr />
                                <Card.Text>主要功能: 根据统计学知识，探索学校内可能存在的问题，量化指标，给出建议</Card.Text>
                                <hr />
                                <Card.Text>亮点: 提高成绩、贫困生帮扶、七选三推荐</Card.Text>
                            </Card.Body>
                        </Card>
                    </div>
                </div>
            </div>
        );
    }
}
