import React, { Component } from 'react';
import { Card , DropdownButton, Dropdown } from 'react-bootstrap';
import Ec from './Ec';
import Intro from './Intro';
import jsonG1TotalRank from '../data/grade/school/grade1_total_rank.json';
import jsonG2TotalRank from '../data/grade/school/grade2_total_rank.json';
import jsonG3TotalRank from '../data/grade/school/grade3_total_rank.json';
import jsonG1Rank from '../data/grade/school/grade1_sub_rank.json';
import jsonG2Rank from '../data/grade/school/grade2_sub_rank.json';
import jsonG3Rank from '../data/grade/school/grade3_sub_rank.json';

export default class extends Component {
    constructor(props) {
        super(props);
        this.state = {
            subName: undefined,
        }
        this.option = null;
        this.subArr = ['总分', '语文', '数学', '英语', '政治', '历史', '地理', '物理', '化学', '生物'];
    }
    chooseSub(subName) {
        this.setOption(subName)
    }
    setOption(subName) {
        let series = [];
        let cnt = 3;
        let defaultLegendSelected = {};
        if (subName === '总分') {
            for (let claName in jsonG1TotalRank) {
                defaultLegendSelected[claName] = cnt>0?true:false;
                cnt --;
                series.push({
                    type: 'line',
                    name: claName,
                    data: jsonG1TotalRank[claName]
                });
            }
            for (let claName in jsonG2TotalRank) {
                defaultLegendSelected[claName] = cnt>0?true:false;
                series.push({
                    type: 'line',
                    name: claName,
                    data: jsonG2TotalRank[claName]
                });
            }
            for (let claName in jsonG3TotalRank) {
                defaultLegendSelected[claName] = cnt>0?true:false;
                series.push({
                    type: 'line',
                    name: claName,
                    data: jsonG3TotalRank[claName]
                });
            }
        } else {
            for (let claName in jsonG1Rank[subName]) {
                defaultLegendSelected[claName] = cnt>0?true:false;
                cnt --;
                series.push({
                    type: 'line',
                    name: claName,
                    data: jsonG1TotalRank[claName]
                });
            }
            for (let claName in jsonG2Rank[subName]) {
                defaultLegendSelected[claName] = cnt>0?true:false;
                series.push({
                    type: 'line',
                    name: claName,
                    data: jsonG2TotalRank[claName]
                });
            }
            for (let claName in jsonG3Rank[subName]) {
                defaultLegendSelected[claName] = cnt>0?true:false;
                series.push({
                    type: 'line',
                    name: claName,
                    data: jsonG3TotalRank[claName]
                });
            }
        }
        this.option = {
            color: ['#749aa0', '#df6b66', '#e79d88', '#8cc1aa', '#ec7e55', '#72a375', '#efdd7d', '#71B9BC', '#7189aa', '#90CA8F', '#F59F48'],
            title: {
                text: '2018-1学期期中考试 / ' + subName,
                left: 'center',
                textStyle: {
                    fontWeight: 400,
                    fontSize: 15,
                }
            },
            grid: {
                left: 0,
                right: 0,
                top: '16%',
                bottom: '14%',
                containLabel: true
            },
            legend: {
                show: true,
                type: 'scroll',
                bottom: 'bottom',
                selected: defaultLegendSelected,
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    axis: 'x',
                    type: 'shadow'
                },
                formatter: (params) => {
                    let resArr = ['班级排名: ' + params[0].name];
                    for (let i = 0; i < params.length; i ++) {
                        resArr.push(params[i].marker + params[i].seriesName + ' 年级排名: ' + params[i].data);
                    }
                    return resArr.join('<br/>');
                }
            },
            xAxis: {
                name: '班级排名',
                nameLocation: 'center',
                type: 'category',
                axisTick: {
                    show: false
                },
                axisPointer: {
                    type: 'shadow'
                },
                axisLabel: {
                    margin: 0,
                },
                data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
            },
            yAxis: {
                name: '年级排名',
                nameLocation: 'start',
                min: 1,
                inverse: true,
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
                    formatter: '{value}名'
                },
            }, 
            series: series
        };
        this.setState({
            subName: subName
        });
    }
    componentWillMount() {
        this.setOption('总分');
    }
    render() {
        return (
            <Card>
                <Card.Header>
                    <h4>1-3-4 班级排名对比</h4>
                    <div className='flex-space-between align-items-center'>
                        <DropdownButton className='ml-2' bsPrefix='drop-down-btn' alignRight title="选择科目">
                            {this.subArr.map((items, index) => {
                                return <Dropdown.Item
                                    key={index}
                                    bsPrefix='drop-down-items'
                                    onClick={this.setOption.bind(this, items)}>{items}</Dropdown.Item>;
                            })}
                        </DropdownButton>
                        <div>
                            <Intro content={[
                                '设计理念: 左上排名高，右下排名低，下降越快表示该班级学生水平差异越大，默认显示三个班级',
                                '功能: 通过比较班级曲线的下降幅度，可以了解班级学生的成绩是否两极分化严重；同时，横向比较各班级的排名曲线，也能了解班级教学质量的差异'
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
