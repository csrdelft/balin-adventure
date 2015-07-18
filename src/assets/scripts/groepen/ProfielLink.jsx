let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let PropTypes = require('react-router').PropTypes;

let Civikaartje = require("./Civikaartje");
let {Link} = require('react-router');

class ProfielLink extends React.Component {

  static get propTypes() {
    return {
      pk: React.PropTypes.string.isRequired,
      name: React.PropTypes.string
    };
  }

  static get contextTypes() {
    return {
      router: React.PropTypes.func.isRequired
    }
  }

  constructor(props, context) {
    super(props, context);
    this.pk = props.pk;
    this.name = props.children;

    // initial state
		this.state = {
      show_civikaartje: false
    };

    this.link = this.link.bind(this);
    this.unlink = this.unlink.bind(this);
  }

  link() {
    this.setState({
      show_civikaartje: true
    });
  }

  unlink() {
  //Uses delay to let animation finish before hiding element
    const delay = 500;
    setTimeout(() => {
      this.setState({
        show_civikaartje: false
      });
    }, delay);
  }

  render_civikaartje() {
    if(this.state.show_civikaartje) {
      return (
       <div className="profielLinkHover" onMouseLeave={this.unlink.bind(this)} >
         <Civikaartje pk={this.pk} />
       </div>
      );
    } else {
      return <div></div>;
    }
  }

  render() {
    if(true) {
      return (
       <div className="profielLinkDiv">
         <Link className="profielLinkName" to="profiel-detail" params={{pk: this.pk}} onMouseEnter={this.link.bind(this)}>
           { this.name }
         </Link>
         {this.render_civikaartje()}
       </div>
      );
    } else {
      return <p>Loading...</p>;
    }
  }
}

module.exports = ProfielLink;
