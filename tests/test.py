#Louis DeVictoria
# Click Testing

from click.testing import CliRunner
from scripts.vars_builder import cli, collect
from scripts.render import render_cfg

def test_cli():
	runner = CliRunner()
	result = runner.invoke(collect, input='cisco\n1.1.1.1\n10.0.0.0/16\nPerimeter81\n2.2.2.2\n10.255.0.0/16\nPRESHARE\naes256\nsha256\n14\n8\n1\n10\ntrue\n65000\n169.254.1.1\n65100\n169.254.1.2\n')
	print(result.stdout)
	return result



