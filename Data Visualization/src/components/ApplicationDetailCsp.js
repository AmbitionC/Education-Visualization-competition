import React from 'react';
import { Table , Input , Button , Icon } from 'antd';
import Highlighter from 'react-highlight-words';
import jsonData from '../data/ori_data/csp.json';
 
export default class extends React.Component {
    state = {
        searchText: '',
    };
    getColumnSearchProps = (dataIndex) => ({
        filterDropdown: ({setSelectedKeys, selectedKeys, confirm, clearFilters}) => (
        <div style={{ padding: 8 }}>
            <Input
            ref={node => { this.searchInput = node; }}
            value={selectedKeys[0]}
            onChange={e => setSelectedKeys(e.target.value ? [e.target.value] : [])}
            onPressEnter={() => this.handleSearch(selectedKeys, confirm)}
            style={{ width: 188, marginBottom: 8, display: 'block' }}
            />
            <Button
            type="primary"
            onClick={() => this.handleSearch(selectedKeys, confirm)}
            icon="search"
            size="small"
            style={{ width: 90, marginRight: 8 }}
            >
            查找
            </Button>
            <Button
            onClick={() => this.handleReset(clearFilters)}
            size="small"
            style={{ width: 90 }}
            >
            重置
            </Button>
        </div>
        ),
        filterIcon: filtered => <Icon type="search" style={{ color: filtered ? '#1890ff' : undefined }} />,
        onFilter: (value, record) => record[dataIndex].toString().toLowerCase().includes(value.toLowerCase()),
        onFilterDropdownVisibleChange: (visible) => {
        if (visible) {
            setTimeout(() => this.searchInput.select());
        }
        },
        render: (text) => (
        <Highlighter
            highlightStyle={{ backgroundColor: '#ffc069', padding: 0 }}
            searchWords={[this.state.searchText]}
            autoEscape
            textToHighlight={text.toString()}
        />
        ),
    })

    handleSearch = (selectedKeys, confirm) => {
        confirm();
        this.setState({ searchText: selectedKeys[0] });
    }

    handleReset = (clearFilters) => {
        clearFilters();
        this.setState({ searchText: '' });
    }

    render() {
        const columns = [{
            title: 'ID',
            dataIndex: 'ID',
            key: 'ID',
            width: '20%',
            ...this.getColumnSearchProps('ID'),
        }, {
            title: '姓名',
            dataIndex: 'name',
            key: 'name',
            width: '20%',
            ...this.getColumnSearchProps('name'),
        }, {
            title: '性别',
            dataIndex: 'gender',
            key: 'gender',
            width: '20%',
            ...this.getColumnSearchProps('gender'),
        }, {
            title: '消费时间',
            dataIndex: 'time',
            key: 'time',
            width: '20%',
            ...this.getColumnSearchProps('time'),
        }, {
            title: '消费金额',
            dataIndex: 'money',
            key: 'money',
            width: '20%',
            ...this.getColumnSearchProps('money'),

        }];
        return <Table columns={columns} dataSource={jsonData} />;
    }
}
