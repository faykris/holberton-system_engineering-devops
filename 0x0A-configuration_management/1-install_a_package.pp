# install puppet-lint in version 2.1.1
package {'puppet-lint':
  ensure   => '2.1.1',
  provider => gem,
}
