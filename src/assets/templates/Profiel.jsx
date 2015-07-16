var InlineInput = require("partials/InlineInput");
var _ = require("underscore");
var React = require("react");

function template(self, p) {
  // helper to make setters for profiel attributes
  function setter(attr) {
    return (v) => self.setState(_.extend(self.state.profiel, {[attr]: v}));
  }

  // actual template based on the state
  return (
    <div>
      <h1>
        <InlineInput value={p.voornaam} setter={setter("voornaam")}/>
        &nbsp;
        <InlineInput value={p.tussenvoegsel} setter={setter("tussenvoegsel")}/>
        &nbsp;
        <InlineInput value={p.achternaam} setter={setter("achternaam")}/>
      </h1>
      <h3>
        A.K.A.
        &nbsp;
        <InlineInput value={p.nickname} setter={setter("nickname")}/>
      </h3>
      <div className="gegevens">
        <table className="table table-bordered">
          <tr>
            <th>Verticale</th>
            <td>{ p.verticale.naam }</td>
          </tr>
          <tr>
            <th>Kring</th>
            <td>{ p.kring.naam }</td>
          </tr>
        </table>
      </div>

      <div className="commissies">
        <h2>Commissies</h2>
        <table className="table table-bordered">
          <tbody>
          { _.map(p.commissies, (c, i) =>
            <tr key={i}><td>{ c.naam }</td></tr>
          )}
          </tbody>
        </table>

        <h2>Werkgroepen</h2>
        <table className="table table-bordered">
          <tbody>
          { _.map(p.werkgroepen, (c, i) =>
            <tr key={i}><td>{ c.naam }</td></tr>
          )}
          </tbody>
        </table>

        <h2>Overige Groepen</h2>
        <table className="table table-bordered">
          <tbody>
          { _.map(p.groepen, (c, i) =>
            <tr key={i}><td>{ c.naam }</td></tr>
          )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

module.exports = template;
