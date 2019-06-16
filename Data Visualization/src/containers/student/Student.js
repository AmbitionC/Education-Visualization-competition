import React from 'react';
import { InputGroup , FormControl , Button , OverlayTrigger , Popover } from 'react-bootstrap';
import StudentInfo from '../../components/StudentInfo1.js'
import StudentAttendance1 from '../../components/StudentAttendance1.js'
// import StudentAttendance2 from '../../components/StudentAttendance2.js'
import StudentAttendance3 from '../../components/StudentAttendance3.js'
// import StudentAttendance4 from '../../components/StudentAttendance4.js'
// import StudentAttendance5 from '../../components/StudentAttendance5.js'
import StudentScore1 from '../../components/StudentScore1.js'
// import StudentScore2 from '../../components/StudentScore2.js'
import StudentScore3 from '../../components/StudentScore3.js'
import StudentScore4 from '../../components/StudentScore4.js'
import StudentScore5 from '../../components/StudentScore5.js'
import StudentScore6 from '../../components/StudentScore6.js'
import StudentScore7 from '../../components/StudentScore7.js'
import StudentScore8 from '../../components/StudentScore8.js'
import StudentScore9 from '../../components/StudentScore9.js'
import StudentScore10 from '../../components/StudentScore10.js'
import StudentScore11 from '../../components/StudentScore11.js'
import StudentScore12 from '../../components/StudentScore12.js'
// import StudentScore13 from '../../components/StudentScore13.js'
import StudentConsumption1 from '../../components/StudentConsumption1.js'
import StudentConsumption2 from '../../components/StudentConsumption2.js'

function Head(props) {
    return (
        <div className='header-body'>
            <div className='row'>
                <div className='col-12 col-lg-9'>
                    <h6 className='header-pretitle'>{props.pretitle}</h6>
                    <h1 className='header-title'>{props.title}</h1>
                </div>
                <div className='col-12 col-lg-3 flex-direction-col justify-content-center'>
                    <InputGroup size='sm'>
                        <FormControl
                        placeholder="请输入学生ID"
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

export default function(){
    return (
        <React.Fragment>
            <Head pretitle='学生画像' title='No.14459 李某某' />
            <div className='row mb-3'>
                <div className='col-12 col-lg-3'>
                    <StudentInfo />
                </div>
                <div className='col- col-lg-4'>
                    <StudentScore12 />
                </div>
                <div className='col-12 col-lg-5'>
                    <StudentScore1 />
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col-12 col-lg-4'>
                    <StudentScore3 />
                </div>
                <div className='col-12 col-lg-4'>
                    <StudentScore4 />
                </div>
                <div className='col-12 col-lg-4'>
                    <StudentScore5 />
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col-12 col-lg-4'>
                    <StudentScore6 />
                </div>
                <div className='col-12 col-lg-4'>
                    <StudentScore7 />
                </div>
                <div className='col-12 col-lg-4'>
                    <StudentScore8 />
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col-12 col-lg-4'>
                    <StudentScore9 />
                </div>
                <div className='col-12 col-lg-4'>
                    <StudentScore10 />
                </div>
                <div className='col-12 col-lg-4'>
                    <StudentScore11 />
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col-12 col-lg-8'>
                    <StudentAttendance3 />
                </div>
                <div className='col-12 col-lg-4'>
                    <StudentAttendance1 />
                </div>
            </div>
            <div className='row mb-3'>
                <div className='col-12 col-lg-4'>
                    <StudentConsumption2 />
                </div>
                <div className='col-12 col-lg-8'>
                    <StudentConsumption1 />
                </div>
            </div>
        </React.Fragment>
    )
}