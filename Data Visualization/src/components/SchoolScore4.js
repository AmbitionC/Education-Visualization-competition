import React, { Component } from 'react';
import { Card , Dropdown , DropdownButton } from 'react-bootstrap';
import Ec from './Ec';
import Intro from './Intro';
import subSegmentJson from '../data/grade/school/sub_score_grade_segment.json';
import totalSegmentJson from '../data/grade/school/total_score_grade_segment.json';

export default class extends Component {
    constructor(props) {
        super(props);
        this.state = {
            examName: undefined,
            subName: undefined,
        };
        this.option = null;
    }
    examName = [
        "2016学年度第一学期期中考试",
        "2016学年度第一学期期末总评",
        "2016学年度第一学期期末考试",
        "2016学年度第二学期总评",
        "2016学年度第二学期期中考试",
        "2016学年度第二学期期末考试",
        "2017学年度第一学期平时成绩1",
        "2017学年度第一学期平时成绩2",
        "2017学年度第一学期期中考试",
        "2017学年度第一学期期末总评",
        "2017学年度第一学期期末考试",
        "2017学年度第二学期平时成绩2",
        "2017学年度第二学期期中考试",
        "2017学年度第二学期期末考试",
        "2017学年第二学期期末总评",
        "2017学年第二学期高一二平时成绩1",
        "2018-1学期期中考试",
        "2018-2019新高一7月测试",
        "2018学年度第一学期平时成绩1",
        "2018学年第一学期高三五校联考",
        "2018学年第一学期高三十校联考"
    ];
    subName = [
        '总分', '语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理', '技术'
    ];
    chooseExam(idx) {
        this.setOption(this.examName[idx], this.state.subName);
    }
    chooseSub(idx) {
        this.setOption(this.state.examName, this.subName[idx]);
    }
    setOption(examName, subName) {
        let className = [];
        let oriData;
        let nameMap;
        let data = [];
        if (subName === '总分') {
            oriData = totalSegmentJson.data;
            nameMap = [
                ['≤100分'],
                ['100-200分'],
                ['200-300分'],
                ['300-400分'],
                ['400-500分'],
                ['500-600分'],
                ['600-700分'],
                ['700-800分'],
                ['≥800分'],
            ];
            for (let i = 0; i < 9; i ++) {
                data.push([]);
            }
        } else {
            oriData = subSegmentJson.data;
            nameMap = [
                ['≤40分'],
                ['40-60分'],
                ['60-70分'],
                ['70-80分'],
                ['80-90分'],
                ['≥90分'],
            ];
            for (let i = 0; i < 6; i ++) {
                data.push([]);
            }
        }
        for (let i = 0; i < oriData.length; i ++) {
            let singleData = oriData[i];
            let len = singleData.length;
            if (subName === '总分') {
                if (singleData[0] === examName) {
                    className.push(singleData[1]);
                    for (let j = 0; j < len - 2; j ++) {
                        data[j].push(singleData[len - 1 - j]);
                    }
                }
            } else {
                if (singleData[0] === examName && singleData[1] === subName) {
                    className.push(singleData[2]);
                    for (let j = 0; j < len - 3; j ++) {
                        data[j].push(singleData[len - 1 - j]);
                    }
                }
            }
        }
        const option = {
            // color: ['#749aa0', '#df6b66', '#e79d88', '#8cc1aa', '#ec7e55', '#72a375', '#efdd7d', '#71B9BC', '#7189aa', '#90CA8F', '#F59F48'],
            color: ['#df6b66', '#ec7e55', '#e79d88', '#efdd7d', '#8cc1aa', '#72a375', '#71b9bc', '#749aa0', '#7189aa'],
            title: {
                text: examName + ' / ' + subName,
                left: 'center',
                textStyle: {
                    fontWeight: 400,
                    fontSize: 15,
                }
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    axis: 'x',
                    type: 'shadow'
                },
            },
            legend: {
                bottom: 'bottom',
                type: 'scroll',
            },
            toolbox: {
                feature: {
                    magicType: {
                        type: ['stack', 'tiled']
                    },
                }
            },
            grid: {
                left: 0,
                right: 0,
                top: '15%',
                bottom: '12%',
                containLabel: true
            },
            xAxis: {
                axisTick: {
                    show: false
                },
                axisPointer: {
                    type: 'shadow'
                },
                axisLabel: {
                    margin: 0,
                },
                data: className
            },
            yAxis: {
                axisTick: {
                    show: false
                },
                splitLine: {
                    lineStyle: {
                        color: '#eeeeee',
                        type: 'dashed'
                    }
                },
                axisLabel: {
                    formatter: '{value}人'
                },
            },
            series: (function (d) {
                let res = [];
                for (let i = 0; i < d.length; i ++) {
                    res.push({
                        type: 'bar',
                        name: nameMap[i],
                        stack: 'segment',
                        data: d[i]
                    });
                }
                return res;
            })(data)
        };
        this.option = option;
        this.setState({
            examName: examName,
            subName: subName,
        });
    }
    componentWillMount() {
        this.setOption(this.examName[0], this.subName[0])
    }
    render() {
        return (
            <Card>
                <Card.Header>
                    <h4>1-3-5 成绩段人数分布</h4>
                    <div className='flex-space-between align-items-center'>
                        <DropdownButton className='ml-2' bsPrefix='drop-down-btn' alignRight title="选择考试">
                            {this.examName.map((items, index) => {
                                return <Dropdown.Item
                                    key={index}
                                    bsPrefix='drop-down-items'
                                    onClick={this.chooseExam.bind(this, index)}>{items}</Dropdown.Item>;
                            })}
                        </DropdownButton>
                        <DropdownButton className='ml-2' bsPrefix='drop-down-btn' alignRight title="选择科目">
                            {this.subName.map((items, index) => {
                                return <Dropdown.Item
                                    key={index}
                                    bsPrefix='drop-down-items'
                                    onClick={this.chooseSub.bind(this, index)}>{items}</Dropdown.Item>;
                            })}
                        </DropdownButton>
                        <div>
                            <Intro content={[
                                '设计理念: 默认为堆叠图，以对比各班级学生在各个分数段的人数；切换到平铺后，可对比班级中各个分数段的人数分布情况',
                                '功能: 通过分数段人数的对比，可以了解到班级中学生的水平分布情况，有助于班主任和科任教师根据班级的实际情况作出相应调整'
                                ]}/>
                        </div>
                    </div>
                </Card.Header>
                <Card.Body>
                    <Ec option={this.option} h='320px' resetOption={true}/>
                </Card.Body>
            </Card>
        );
    }
}