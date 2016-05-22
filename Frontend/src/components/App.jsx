import React, { Component, PropTypes } from 'react';
import { Row, Col, Menu, Dropdown, Icon, Button, Card, Input, Collapse } from 'antd';
import { Link } from 'react-router';
const SubMenu = Menu.SubMenu;
const Panel = Collapse.Panel;

const Provider = React.createClass({
	render: function() {
		var APIList = [];
		this.props.provider.APIs.forEach(function(element, index, array) {
			APIList.push(
				<Button>{(element.type == "query") ? <Icon type="tag" /> : <Icon type="share-alt" />}{element.name}</Button>);
		});
		return <div className="APIbutton-container">{APIList}</div>
	},
});

const MainLayout = React.createClass({
	getInitialState: function() {
		// fetch(Server + '/room/' + this.props.id + '/')
		// 	.then(function(res) {
		// 		if (res.ok) {
		// 			return res.json();
		// 		};
		// 	})
		// 	.then(function(json) {
		// 		this.setState({
		// 			loading: 0,
		// 			category: undefined,
		// 			name: json.name,
		// 			location: json.location,
		// 			capacity: json.capacity,
		// 			provider_name: json.provider_name,
		// 			open_hours: json.open_hours,
		// 			img: json.img,
		// 		});
		// 	}.bind(this));
		return {
			providers: [
				{
					id: 1,
					name: "HackProvider1",
					baseurl: "",
					APIs:[
						{
							id: 1,
							name: "时间",
							slug: "aaaaa",
							type: "query",
							args: [],
							return: [],
							authority: [],
						},
						{
							id: 2,
							name: "时间时间时间时间",
							slug: "aaaaa",
							type: "query",
							args: [],
							return: [],
							authority: [],
						},
						{
							id: 3,
							name: "时间",
							slug: "aaaaa",
							type: "query",
							args: [],
							return: [],
							authority: [],
						},
						{
							id: 4,
							name: "时间",
							slug: "aaaaa",
							type: "query",
							args: [],
							return: [],
							authority: [],
						},
						{
							id: 5,
							name: "时间",
							slug: "aaaaa",
							type: "query",
							args: [],
							return: [],
							authority: [],
						}
					],
				},
				{
					id: 2,
					name: "HackProvider2",
					baseurl: "",
					APIs:[
						{
							id: 6,
							name: "时间",
							slug: "aaaaa",
							type: "query",
							args: [],
							return: [],
							authority: [],
						},
						{
							id: 7,
							name: "时间时间时间时间",
							slug: "aaaaa",
							type: "query",
							args: [],
							return: [],
							authority: [],
						},
						{
							id: 8,
							name: "时间",
							slug: "aaaaa",
							type: "query",
							args: [],
							return: [],
							authority: [],
						},
						{
							id: 9,
							name: "时间",
							slug: "aaaaa",
							type: "query",
							args: [],
							return: [],
							authority: [],
						},
						{
							id: 10,
							name: "时间",
							slug: "aaaaa",
							type: "query",
							args: [],
							return: [],
							authority: [],
						}
					],
				},
				{
					id: 3,
					name: "HackProvider3",
					baseurl: "",
					APIs:[
						{
							id: 11,
							name: "时间",
							slug: "aaaaa",
							type: "query",
							args: [],
							return: [],
							authority: [],
						},
						{
							id: 12,
							name: "时间时间时间时间",
							slug: "aaaaa",
							type: "query",
							args: [],
							return: [],
							authority: [],
						},
						{
							id: 13,
							name: "时间",
							slug: "aaaaa",
							type: "query",
							args: [],
							return: [],
							authority: [],
						},
						{
							id: 14,
							name: "时间",
							slug: "aaaaa",
							type: "query",
							args: [],
							return: [],
							authority: [],
						},
						{
							id: 15,
							name: "时间",
							slug: "aaaaa",
							type: "query",
							args: [],
							return: [],
							authority: [],
						}
					],
				},
			],
			logics: [
				{
					id: 1,
					name: "Logic 1",
					describe: "IF 物联网主机.灯光状态 = 0",
					Q:[],
					A:[],
					T:[],
					TimeStamp:100000,
				},
				{
					id: 2,
					name: "Logic 2",
					describe: "IF 物联网主机.灯光状态 = 0",
					Q:[],
					A:[],
					T:[],
					TimeStamp:100000,
				},
				{
					id: 3,
					name: "Logic 3",
					describe: "IF 物联网主机.灯光状态 = 0 and 物联网主机.门锁状态 = 0",
					Q:[],
					A:[],
					T:[],
					TimeStamp:100000,
				},
				{
					id: 2,
					name: "Logic 2",
					describe: "IF 物联网主机.灯光状态 = 0",
					Q:[],
					A:[],
					T:[],
					TimeStamp:100000,
				},
				{
					id: 3,
					name: "Logic 3",
					describe: "IF 物联网主机.灯光状态 = 0 and 物联网主机.门锁状态 = 0",
					Q:[],
					A:[],
					T:[],
					TimeStamp:100000,
				},
			],
			logic: {
				id: 1,
				name: "Logic 1",
				describe: "IF 物联网主机.灯光状态 = 0 and 物联网主机.门锁状态 = 0",
				Q:[],
				A:[],
				T:[],
				TimeStamp:100000,
			},
		};
	},
	render: function() {
		var ProviderList = [];
		this.state.providers.forEach(function(element, index, array) {
			ProviderList.push(
				<Panel key={index} header={element.name}>
					<Provider provider={element}/>
				</Panel>);
		});

		return <div id="MainLayout">
			<Row>
				<Col span={4} id="MainLayout-MenuLayout">
					<img id="logo" src={require("../image/logo.png")} />
					<Button id="import-provider" size="small">
						Import Provider
					</Button>
					<div id="menu">
						<Collapse accordion>
							{ProviderList}
						</Collapse>
					</div>
				</Col>
				<Col span={20} id="MainLayout-MainLayout">
					{this.props.children && React.cloneElement(this.props.children, {
						logics: this.state.logics,
						logic: this.state.logic,
					})}
				</Col>
			</Row>
		</div>
	},
});

const LogicCard = React.createClass({
	render: function() {
		return <Col span={8} className="card-container">
			<Card title={this.props.logic.name}></Card>
		</Col>
	},
});

const LogicListLayout = React.createClass({
	render: function() {
		var LogicList = [];
		this.props.logics.forEach(function(element, index, array) {
			LogicList.push(
				<Col span={8} className="card-container">
					<Link to={"/logic/" + element.id}>
						<Card title={element.name} extra={<Icon type="edit" />}>
							<div>{element.describe}</div>
						</Card>
					</Link>
				</Col>);
		});

		return <div id="LogicListLayout">
			<div id="LogicListLayout-header">
				<Row>
					<Col span={12}>
						<h2>Your IFs</h2>
					</Col>
					<Col span={12} style={{textAlign: "right",}}>
						<Button type="primary" shape="circle" icon="plus" />
					</Col>
				</Row>
			</div>
			<Row gutter={32}>
				{LogicList}
			</Row>
		</div>
	},
});

const LogicLayout = React.createClass({
	render: function() {
		return <div id="LogicLayout">
			<div id="LogicLayout-header">
				<Row>
					<Col span={12}>
						<h2>IF [LOGIC NAME]</h2>
					</Col>
					<Col span={12} style={{textAlign: "right",}}>
						<Button type="primary" shape="circle" icon="plus" />
					</Col>
				</Row>
			</div>
			<Row>
				<Col span={24}>
					<Card title={<Input id="LogicLayout-name" defaultValue={this.props.logic.name} placeholder="Logic Name"/>}>
						<Row type="flex" align="top">
							<Col span={6} className="LogicLayout-keyword">
								<h1>IF</h1>
							</Col>
							<Col span={14} id="if-container">
								s<br/>s<br/>s<br/>s<br/>s<br/>s<br/>s<br/>
							</Col>
							<Col span={6} className="LogicLayout-keyword">
								<h1>THEN</h1>
							</Col>
							<Col span={14} id="then-container">
							</Col>
						</Row>
					</Card>
				</Col>
			</Row>
		</div>
	},
});

export default {
	"MainLayout": MainLayout,
	"LogicListLayout": LogicListLayout,
	"LogicLayout": LogicLayout
};
