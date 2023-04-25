#Louis DeVictoria
# Test to run the vars_builder cli script to test
import click.testing
from click.testing import CliRunner
from scripts.vars_builder import cli, collect
runner = CliRunner()
def test_cli():
	test_cisco()
	test_fortinet()
	test_paloalto()
	test_mikrotik()


def test_cisco():
	cisco = runner.invoke(collect, input='cisco\n1.1.1.1\n10.0.0.0/16\nPerimeter81\n2.2.2.2\n10.255.0.0/16\nPRESHARE1\nPRESHARE1\naes256\nsha256\n14\n8\n1\n10\ntrue\n65000\n169.254.1.1\n65100\n169.254.1.2\n')
	return cisco
def test_fortinet():
	fortinet = runner.invoke(collect, input='fortinet\n1.1.1.1\n10.0.0.0/16\nPerimeter81\n2.2.2.2\n10.255.0.0/16\nPRESHARE1\nPRESHARE1\naes256\nsha256\n14\n8\n1\n10\ntrue\n65000\n169.254.1.1\n65100\n169.254.1.2\n')
	return fortinet
def test_paloalto():
	paloalto = runner.invoke(collect, input='paloalto\n1.1.1.1\n10.0.0.0/16\nPerimeter81\n2.2.2.2\n10.255.0.0/16\nPRESHARE1\nPRESHARE1\naes256\nsha256\n14\n8\n1\n10\ntrue\n65000\n169.254.1.1\n65100\n169.254.1.2\n')
	return paloalto
def test_mikrotik():
	mikrotik = runner.invoke(collect, input='mikrotik\n1.1.1.1\n10.0.0.0/16\nPerimeter81\n2.2.2.2\n10.255.0.0/16\nPRESHARE1\nPRESHARE1\naes256\nsha256\n14\n8\n1\n10\ntrue\n65000\n169.254.1.1\n65100\n169.254.1.2\n')
	return mikrotik

	#result = runner.invoke(collect, input='mikrotik\n1.1.1.1\n10.0.0.0/16\nPerimeter81\n2.2.2.2\n10.255.0.0/16\nPRESHARE1\nPRESHARE1\naes256\nsha256\n14\n8\n1\n10\ntrue\n65000\n169.254.1.1\n65100\n169.254.1.2\n')
	#print(result.stdout)
	#return result

if __name__ == '__main__':
	test_cli()
