import React from 'react';
import { Card , DropdownButton , Dropdown } from 'react-bootstrap';
import Ec from './Ec';
import Intro from './Intro';
import jsonG1BoxData from '../data/grade/school/grade1_box_data.json';
import jsonG1BoxOutlier from '../data/grade/school/grade1_box_outlier.json';
import jsonG2BoxData from '../data/grade/school/grade2_box_data.json';
import jsonG2BoxOutlier from '../data/grade/school/grade2_box_outlier.json';
import jsonG3BoxData from '../data/grade/school/grade3_box_data.json';
import jsonG3BoxOutlier from '../data/grade/school/grade3_box_outlier.json';

export default class extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            grade: undefined
        };
        this.option = null;
    }
    setOption(grade) {
        let jsonBoxData;
        let jsonBoxOutlier;
        if (grade === '高一') {
            jsonBoxData = jsonG1BoxData;
            jsonBoxOutlier = jsonG1BoxOutlier;
        } else if (grade === '高二') {
            jsonBoxData = jsonG2BoxData;
            jsonBoxOutlier = jsonG2BoxOutlier;
        } else if (grade === '高三') {
            jsonBoxData = jsonG3BoxData;
            jsonBoxOutlier = jsonG3BoxOutlier;
        } else {
            return undefined;
        }
        let boxObj = {};
        const subArr = ['语文','数学','英语','物理','化学','生物','政治','历史','地理','技术'];
        for (let i = 0; i < jsonBoxData.index.length; i ++) {
            if (!boxObj[jsonBoxData.index[i]]) {
                boxObj[jsonBoxData.index[i]] = [ [], [], [], [], [], [], [], [], [], [] ];
            }
            const subIdx = subArr.indexOf(jsonBoxData.data[i][5]);
            if (subIdx > -1 ) {
                boxObj[jsonBoxData.index[i]][subIdx] = jsonBoxData.data[i];
            }
        }
        let outObj = {};
        for (let i = 0; i < jsonBoxOutlier.index.length; i ++) {
            if (!outObj[jsonBoxOutlier.index[i]]) {
                outObj[jsonBoxOutlier.index[i]] = [];
            }
            if (jsonBoxOutlier.data[i][1] !== '总分') {
                outObj[jsonBoxOutlier.index[i]].push([jsonBoxOutlier.data[i][1], jsonBoxOutlier.data[i][0]])
            }
        }
        let series = [];
        for (let examName in boxObj) {
            series.push({
                name: examName,
                type: 'boxplot',
                itemStyle: {
                    borderColor: '#7189aa'
                },
                data: boxObj[examName],
                tooltip: {
                    formatter: function (param) {
                        return [
                            param.name,
                            '上边界: ' + param.data[5],
                            '上四分位数: ' + param.data[4],
                            '中位数: ' + param.data[3],
                            '下四分位数: ' + param.data[2],
                            '下边界: ' + param.data[1]
                        ].join('<br/>');
                    }
                }
            });
            if (outObj[examName]) {
                series.push({
                    name: examName,
                    type: 'scatter',
                    itemStyle: {
                        color: '#e79d88'
                    },
                    data: outObj[examName]
                });
            }
        }
        this.option = {
            title: {
                text: '2018-1学期期中考试 / ' + grade,
                left: 'center',
                textStyle: {
                    fontWeight: 400,
                    fontSize: 15,
                }
            },
            legend: {
                show: false
            },
            tooltip: {},
            grid: {
                left: 0,
                right: 0,
                top: '15%',
                bottom: '8%',
                containLabel: true
            },
            xAxis: {
                type: 'category',
                data: subArr,
                boundaryGap: true,
                nameGap: 30,
                splitLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
            },
            yAxis: {
                type: 'value',
                name: '分数',
                splitLine: {
                    show: true,
                    lineStyle: {
                        color: '#eee',
                        type: 'dashed'
                    }
                },
                axisLine: {
                    show: false
                },
                axisTick: {
                    show: false
                }
            },
            series: series
        };
        this.setState({
            grade: grade
        });
    }
    componentWillMount() {
        this.setOption('高一');
    }
    render() {
        return (
            <Card>
                <Card.Header>
                    <h4>1-3-2 年级成绩箱形图</h4>
                    <div className='flex-space-between align-items-center'>
                        <DropdownButton className='ml-2' bsPrefix='drop-down-btn' alignRight title="选择年级">
                            {['高一', '高二', '高三'].map((items, index) => {
                                return <Dropdown.Item
                                    key={index}
                                    bsPrefix='drop-down-items'
                                    onClick={this.setOption.bind(this, items)}>{items}</Dropdown.Item>;
                            })}
                        </DropdownButton>
                        <div>
                            <Intro content={[
                                '设计理念: 箱形图可以直观的展示班级学生的成绩分布情况',
                                '功能: 帮助校领导层了解学校各年级成绩的分布和成绩垫底的学生的具体情况'
                            ]} />
                        </div>
                    </div>
                </Card.Header>
                <Card.Body>
                    <Ec option={this.option} h='240px' resetOption={true}/>
                </Card.Body>
            </Card>
        );
    }
}
