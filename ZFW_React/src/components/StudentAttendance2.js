import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec'
import studentAttendance from '../data/student/Student_Attendance_2.json'

export default function(){
    const option = {
        legend: {
            data: ['学生离校', '班级平均离校', '学校平均离校'],
            selected:{
                '学生离校': true,
                '班级平均离校': false,
                '学校平均离校': true
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
            }
        }],
        polar: {
        },
        series: [
            {
                name: '学生离校',
                type: 'bar',
                itemStyle: {
                    color: '#ff9797'
                },
                data: studentAttendance.student,
                coordinateSystem: 'polar',
            },{
                name: '班级平均离校',
                type: 'bar',
                itemStyle: {
                    color: '#a3d1d1'
                },
                data: studentAttendance.class,
                coordinateSystem: 'polar',
            },{
                name: '学校平均离校',
                type: 'bar',
                itemStyle: {
                    color: '#bebebe'
                },
                data: studentAttendance.school,
                coordinateSystem: 'polar',
            }
        ]
    };
    return (
        <Card>
            <Card.Header>
                <h4>晚间离校时间统计</h4>
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='450px'/>
            </Card.Body>
        </Card>
    )
}