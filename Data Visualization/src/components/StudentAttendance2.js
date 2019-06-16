import React from 'react';
import Ec from './Ec'
import studentAttendance from '../data/student/Student_Attendance_2.json'

export default function(){
    const option = {
        legend: {
            bottom: 'bottom',
            data: ['学生离校', '班级平均离校', '学校平均离校'],
            selected: {
                '学生离校': true,
                '班级平均离校': false,
                '学校平均离校': true,
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
                name: '学生离校',
                type: 'bar',
                itemStyle: {
                    color: '#df6b66'
                },
                data: studentAttendance.student,
                coordinateSystem: 'polar',
            },{
                name: '班级平均离校',
                type: 'bar',
                itemStyle: {
                    color: '#90ca8f'
                },
                data: studentAttendance.class,
                coordinateSystem: 'polar',
            },{
                name: '学校平均离校',
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
        <Ec option={option} h='300px'/>
    )
}