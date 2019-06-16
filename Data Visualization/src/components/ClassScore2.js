import React from 'react';
import { Card , Dropdown , DropdownButton } from 'react-bootstrap';
import Ec from './Ec';
import jsonData from '../data/grade/class/class920_sub_score_peo_num.json';
import jsonData2 from '../data/grade/class/class920_total_score_segment.json';

export default class extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            examName: undefined,
        };
        this.option1 = null;
        this.option2 = null;
        this.examArr = [
            '2016学年度第一学期期中考试',
            '2016学年度第一学期期末考试',
            '2016学年度第一学期期末总评',
            '2016学年度第二学期期中考试',
            '2016学年度第二学期期末考试',
            '2016学年度第二学期总评',
            '2017学年度第一学期期中考试',
            '2017学年度第一学期期末考试',
            '2017学年度第一学期期末总评',
            '2017学年度第二学期期中考试',
            '2017学年度第二学期期末考试',
            '2017学年第二学期期末总评',
            '2018学年第一学期高三十校联考',
            '2018学年第一学期高三五校联考',
            '2018-1学期期中考试'
        ];
    }
    chooseExam(idx) {
        this.setOption(idx);
    }
    setOption(index) {
        const examIndexArr = [0, 215, 395, 563, 786, 1009, 1225, 1414, 1627, 1810, 1939, 2123, 2284, 2412, 2541];
        const data = jsonData.data;
        const end = index===examIndexArr.length-1?data.length:examIndexArr[index+1];
        let subObj = {};
        let curSub = '';
        for (let i = examIndexArr[index]; i < end; i ++) {
            if (!curSub) {
                subObj[data[i][2]] = [examIndexArr[index]];
                curSub = data[i][2];
            }
            if (data[i][2] !== curSub) {
                subObj[curSub].push(i);
                subObj[data[i][2]] = [i];
                curSub = data[i][2];
            }
            if (i === end - 1) {
                subObj[curSub].push(end);
            }
        }
        const subName = ['语文', '数学', '英语', '物理', '化学', '生物', '政治', '历史', '地理', '技术'];
        let series = [];
        for (let i = 0; i < subName.length; i ++) {
            if (subObj[subName[i]]) {
                series.push({
                    type: 'bar',
                    name: subName[i],
                    data: jsonData.data.slice(subObj[subName[i]][0], subObj[subName[i]][1])
                });
            }
        }
        this.option1 = {
            color: ['#7189aa', '#df6b66', '#e79d88', '#8cc1aa', '#749aa0', '#72a375', '#efdd7d', '#71B9BC', '#7189aa', '#90CA8F', '#F59F48'],
            title: {
                text: this.examArr[index],
                left: 'center',
                textStyle: {
                    fontWeight: 400,
                    fontSize: 16,
                }
            },
            grid: {
                left: 0,
                right: '8%',
                top: '15%',
                bottom: '15%',
                containLabel: true
            },
            legend: {
                bottom: 'bottom',
                selectedMode: 'single',
                type: 'scroll',
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    axis: 'x',
                    type: 'shadow'
                },
            },
            xAxis: {
                type: 'category',
                name: '分数',
                data: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121", "122", "123", "124", "125", "126", "127", "128", "129", "130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "140", "141", "142", "143", "144", "145", "146", "147", "148", "149", "150"],
                splitLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
            },
            yAxis: {
                name: '人数',
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
                },
            },
            series: series,
        };
        this.option2 = {
            color: ['#71B9BC'],
            grid: {
                left: 0,
                right: '8%',
                top: '15%',
                bottom: 0,
                containLabel: true
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    axis: 'x',
                    type: 'shadow'
                },
            },
            xAxis: {
                name: '总分',
                type: 'category',
                splitLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                data: ['100-200分', '200-300分', '300-400分', '400-500分', '500-600分', '600-700分', '700分以上']
            },
            yAxis: {
                name: '人数',
                type: 'value',
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
                },
            },
            series: [{
                data: jsonData2.data[index],
                type: 'bar'
            }]
        };
        this.setState({
            examName: this.examArr[index]
        });
    }
    componentWillMount() {
        this.setOption(0);
    }
    render() {
        return (
            <Card>
                <Card.Header>
                    <h4>2-3 成绩人数分布</h4>
                    <div className='flex-space-between align-items-center'>
                        <DropdownButton className='ml-2' bsPrefix='drop-down-btn' alignRight title="选择考试">
                            {this.examArr.map((items, index) => {
                                return <Dropdown.Item
                                    key={index}
                                    bsPrefix='drop-down-items'
                                    onClick={this.chooseExam.bind(this, index)}>{items}</Dropdown.Item>;
                            })}
                        </DropdownButton>
                    </div>
                </Card.Header>
                <Card.Body>
                    <Ec option={this.option1} h='200px' resetOption={true}/>
                    <Ec option={this.option2} h='200px' resetOption={true}/>
                </Card.Body>
            </Card>
        );
    }
}
