use strict;
use warnings;
use diagnostics;

use feature 'say';                                      # Print Function Enabled
use feature 'switch';                                   # Switch Case Enabled
use v5.16;                                              # Perl Version Fixed

print "Hello World\n";

my $name = 'Allen';                                     # String with variable name (scalar)
my $age = 20;                                           # Integer with variable age (scalar)
my ($street,$city) = ('Indiranagar','Bangalore');       # String with Multiple Values (Array)

my $info = "$name lives on \"$street\"";                # Double quotes for additional functionality
$info = qq{$name lives on "$street"};                   # Same as the previous line

my $info2 = <<"END";                                    # String with Multiline
This is a lot 
of information
on multiple lines
END

say $info2;

my $f1 = 1.00096;
my $f2 = 8.12073;

printf("%.3f \n",$f1+$f2);