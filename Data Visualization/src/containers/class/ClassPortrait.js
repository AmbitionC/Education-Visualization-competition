import React, { Component } from 'react';
import { InputGroup , FormControl , Button , OverlayTrigger , Popover } from 'react-bootstrap';
import Tea from '../../components/ClassTeacher';
import Csp from '../../components/ClassCsp';
import Kq from '../../components/ClassKq';
import Score1 from '../../components/ClassScore1';
import Score2 from '../../components/ClassScore2';
import Score3 from '../../components/ClassScore3';
import Score4 from '../../components/ClassScore4';
import Score5 from '../../components/ClassScore5';

function Head(props) {
    return (
        <div className='header-body'>
            <div className='row'>
                <div className='col-12 col-lg-3'>
                    <h6 className='header-pretitle'>{props.pretitle}</h6>
                    <h1 className='header-title'>{props.title}</h1>
                </div>
                <div className='col-12 col-lg-6 justify-content-center align-items-center'>
                    <Tea />
                </div>
                <div className='col-12 col-lg-3 flex-direction-col justify-content-center'>
                    <InputGroup size='sm'>
                        <FormControl
                        placeholder="请输入班级ID"
                        aria-describedby="basic-addon2"
                        />
                        <InputGroup.Append>
                            <Button variant='outline-primary'>确定</Button>
                            <OverlayTrigger
                            trigger="click"
                            placement={'left'}
                            overlay={
                                <Popover>
                                    <span className='text-muted'>因为数据的完备性问题，平台选取较有代表性样例展示，后期根据应用进行拓展</span>
                                </Popover>
                            }
                            >
                                <Button variant="outline-info">说明</Button>
                            </OverlayTrigger>
                        </InputGroup.Append>
                    </InputGroup>
                </div>
            </div>
        </div>
    );
}

export default class extends Component {
    render() {
        return (
            <React.Fragment>
                <Head pretitle='班级画像' title='No.920 高三(08)' />
                <div className='row mb-3'>
                    <div className='col-12 col-lg-6'>
                        <div className='row mb-3'>
                            <div className='col'>
                                <Score4 />
                            </div>
                        </div>
                        <div className='row'>
                            <div className='col'>
                                <Score2 />
                            </div>
                        </div>
                    </div>
                    <div className='col-12 col-lg-6'>
                        <div className='row mb-3'>
                            <div className='col'>
                                <Score3 />
                            </div>
                        </div>
                        <div className='row'>
                            <div className='col'>
                                <Score1 />
                            </div>
                        </div>
                    </div>
                </div>
                <div className='row mb-3'>
                    <div className='col'>
                        <Score5 />
                    </div>
                </div>
                <div className='row mb-3'>
                    <div className='col-12 col-lg-6'>
                        <Csp/>
                    </div>
                    <div className='col-12 col-lg-6'>
                        <Kq/>
                    </div>
                </div>
            </React.Fragment>
        );
    }
}