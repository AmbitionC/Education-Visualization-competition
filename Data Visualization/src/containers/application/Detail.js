import React from 'react';
import { Tabs , Tab } from 'react-bootstrap';
import Stu from '../../components/ApplicationDetailStu';
import Tea from '../../components/ApplicationDetailTeacher';
import Csp from '../../components/ApplicationDetailCsp';
import Kq from '../../components/ApplicationDetailKq';
import Cj from '../../components/ApplicationDetailCj';
import 'antd/dist/antd.css';

export default function () {
    return (
        <Tabs defaultActiveKey="stu">
            <Tab eventKey='stu' title="学生信息">
                <Stu />
            </Tab>
            <Tab eventKey='tea' title="教师信息">
                <Tea />
            </Tab>
            <Tab eventKey='kq' title="考勤明细">
                <span className='text-muted mt-3 mb-3'>注: 由于数据量过大, 仅包含2015年1月1日之后的数据</span>
                <Kq />
            </Tab>
            <Tab eventKey='csp' title="消费明细">
                <span className='text-muted mt-3 mb-3'>注: 由于数据量过大, 仅包含2019年1月1日至2019年1月20日的数据</span>
                <Csp />
            </Tab>
            <Tab eventKey='cj' title="成绩数据">
                <span className='text-muted mt-3 mb-3'>注: 由于数据量过大, 仅包含2018-1学期期中考试的数据</span>
                <Cj />
            </Tab>
        </Tabs> 
    );
}