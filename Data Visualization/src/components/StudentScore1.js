import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec'
import Intro from './Intro';
import StuScore2 from './StudentScore2';
import StuScore13 from './StudentScore13';

export default function(){
    // 展示学生的成绩部分，需要展示学生的每次考试的总分和班级的平均分，以及未来两次考试的预测
    const student_score = [432, 438, 420, 420, 402, 486, 438, 438, 474, 432, 486, 438, 324, 468, 486, 456, 504, 480, 474, 468, 480, 474, 492, 468];
    const class_score = [414, 450, 408, 414, 414, 498, 420, 456, 468, 426, 504, 432, 324, 480, 504, 444, 504, 486, 474, 480, 462, 456, 480, 480];
    const student_score_predict = [432, 438, 420, 420, 402, 486, 438, 438, 474, 432, 486, 438, 324, 468, 486, 456, 504, 480, 474, 468, 480, 474, 492, 468, 473, 482]
    const xlabel = ['2016学年度第一学期期中考试', '2016学年度第一学期考查课总评', '2016学年度第一学期期末考试', '2016学年度第一学期期末总评', '2016学年度第二学期期中考试', '2016学年度第二学期考查课总评', '2016学年度第二学期期末考试', '2016学年度第二学期总评', '2017学年度第一学期期中考试', '2017学年度第一学期平时成绩1', '2017-1学期考察科目总评', '2017学年度第一学期平时成绩2', '\t2017学年度第一学期期末考试', '2017学年度第一学期期末总评', '2017学年第二学期高一二平时成绩1', '2017学年度第二学期期中考试', '2017学年度第二学期平时成绩2', '2017学年度第二学期期末考试', '2017学年第二学期期末总评', '2018学年第一学期高三十校联考', '2018学年第一学期高三五校联考', '2018学年度第一学期平时成绩1', '2018-1学期期中考试', '2018学年度第一学期平时成绩2', '预测成绩1', '预测成绩2'];
    const option = {
        title: {
            text: '总分成绩趋势',
            textStyle: {
                fontSize: 12 
            }
        },
        legend: {
            left: 'right',
            data: ['历史成绩', '班级均分', '预测成绩']
        },
        grid:{
            left: 0,
            right: 0,
            top: '20%',
            bottom: '5%',
            containLabel: true
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                axis: 'x',
                type: 'line'
            }
        },
        xAxis: {
            type: 'category',
            axisTick: {
                show: false
            },
            axisLabel: {
                show: false
            },
            data: xlabel
        },
        yAxis: {
            type: 'value',
            min: 300,
            max: 600,
            axisTick: {
                show: false
            },
            splitLine: {
                lineStyle: {
                    color: '#eeeeee',
                    type: 'dashed'
                }
            }
        },
        series: [{
            name: '预测成绩',
            itemStyle: {
                color: '#df6b66'
            },
            data: student_score_predict,
            type: 'line'
        },{
            name: '历史成绩',
            itemStyle: {
                color: '#90ca8f'
            },
            data: student_score,
            type: 'line'
        },{
            name: '班级均分',
            itemStyle: {
                color: '#787d7b'
            },
            lineStyle: {
                type: 'dashed'
            },
            data: class_score,
            type: 'line'
        }]
    };
    return (
        <Card>
            <Card.Header>
                <h4>3-3 总分趋势</h4>
                <Intro content={[
                    '置信区间: 置信区间范围取决于当前成绩与历次成绩评估结果'
                ]}/>
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='150px' />
                <StuScore2/>
                <StuScore13/>
            </Card.Body>
        </Card>
    )
}