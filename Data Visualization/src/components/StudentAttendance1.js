import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec'
import StudentAttendance2 from './StudentAttendance2';
import studentAttendance from '../data/student/Student_Attendance_1.json'

export default function(){
    const option = {
        legend: {
            bottom: 'bottom',
            data: ['学生到勤', '班级平均到勤', '学校平均到勤'],
            selected: {
                '学生到勤': true,
                '班级平均到勤': true,
                '学校平均到勤': false,
            }
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross'
            },
        },
        angleAxis: {
            scale: 'True',
            type: 'category',
            boundaryGap: false,
            axisTick: {
                alignWithLabel: true
            },
            data: studentAttendance.xlabel,
            z: 10
        },
        radiusAxis: [{
            show: true,
            axisLabel: {
                show: true,
                showMaxLabel: false,
                showMinLabel: false
            },
            axisTick: {
                show: false
            },
            splitLine: {
                lineStyle: {
                    color: '#eeeeee',
                    type: 'dashed'
                }
            }
        }],
        polar: {
            center: ['50%', '48%'],
            radius: '75%'
        },
        series: [
            {
                name: '学生到勤',
                type: 'bar',
                itemStyle: {
                    color: '#df6b66'
                },
                data: studentAttendance.student,
                coordinateSystem: 'polar',
            },{
                name: '班级平均到勤',
                type: 'bar',
                itemStyle: {
                    color: '#90ca8f'
                },
                data: studentAttendance.class,
                coordinateSystem: 'polar',
            },{
                name: '学校平均到勤',
                type: 'bar',
                itemStyle: {
                    color: '#7189aa'
                },
                data: studentAttendance.school,
                coordinateSystem: 'polar',
            }
        ]
    };
    return (
        <Card>
            <Card.Header>
                <h4>3-6 到勤、离勤时间统计</h4>
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='300px'/>
                <StudentAttendance2/>
            </Card.Body>
        </Card>
    )
}