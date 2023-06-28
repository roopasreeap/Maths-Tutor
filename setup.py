##########################################################################
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
###########################################################################

from distutils.core import setup
from glob import glob
setup(name='MathsTutor',
      version='1.0',
      description='Game for learning mathematical operations',
      author='Roopasree AP',
      author_email='roopasreeap@gmail.com',
      url='https://github.com/roopasreeap/Maths-Tutor',
      license = 'GPL-3',
      packages=['MathsTutor'],
      data_files=[('share/maths-tutor/',['icon.jpg', 'data.txt']),

      ('share/maths-tutor/images/',['images/neg8.png']),
      ('share/maths-tutor/images/',['images/positive6.png']),
      ('share/maths-tutor/images/',['images/neg1.png']),
      ('share/maths-tutor/images/',['images/neg10.png']),
      ('share/maths-tutor/images/',['images/positive1.png']),
      ('share/maths-tutor/images/',['images/image1.png']),
      ('share/maths-tutor/images/',['images/neg7.png']),
      ('share/maths-tutor/images/',['images/positive11.png']),
      ('share/maths-tutor/images/',['images/positive4.png']),
      ('share/maths-tutor/images/',['images/neg6.png']),
      ('share/maths-tutor/images/',['images/neg9.png']),
      ('share/maths-tutor/images/',['images/positive5.png']),
      ('share/maths-tutor/images/',['images/positive2.png']),
      ('share/maths-tutor/images/',['images/positive.png']),
      ('share/maths-tutor/images/',['images/positive12.png']),
      ('share/maths-tutor/images/',['images/positive7.png']),
      ('share/maths-tutor/images/',['images/neg3.png']),
      ('share/maths-tutor/images/',['images/positive9.png']),
      ('share/maths-tutor/images/',['images/neg2.png']),
      ('share/maths-tutor/images/',['images/positive8.png']),
      ('share/maths-tutor/images/',['images/neg5.png']),
      ('share/maths-tutor/images/',['images/positive10.png']),

      ('share/maths-tutor/sounds/',['sounds/next_level_6.ogg']),
      ('share/maths-tutor/sounds/',['sounds/got_promotion.ogg']),
      ('share/maths-tutor/sounds/',['sounds/type.ogg']),
      ('share/maths-tutor/sounds/',['sounds/next_level_4.ogg']),
      ('share/maths-tutor/sounds/',['sounds/next_level_0.ogg']),
      ('share/maths-tutor/sounds/',['sounds/next_level_5.ogg']),
      ('share/maths-tutor/sounds/',['sounds/clap.ogg']),
      ('share/maths-tutor/sounds/',['sounds/start.ogg']),
      ('share/maths-tutor/sounds/',['sounds/good.ogg']),
      ('share/maths-tutor/sounds/',['sounds/warning.ogg']),
      ('share/maths-tutor/sounds/',['sounds/wrong_pressed.ogg']),
      ('share/maths-tutor/sounds/',['sounds/ok.ogg']),
      ('share/maths-tutor/sounds/',['sounds/very_good.ogg']),
      ('share/maths-tutor/sounds/',['sounds/excellent.ogg']),
      ('share/maths-tutor/sounds/',['sounds/next_level_1.ogg']),
      ('share/maths-tutor/sounds/',['sounds/next_level_3.ogg']),
      ('share/maths-tutor/sounds/',['sounds/coin.ogg']),
      ('share/maths-tutor/sounds/',['sounds/try_more_fast.ogg']),
      ('share/maths-tutor/sounds/',['sounds/next_level_2.ogg']),

      ('share/applications/',['maths-tutor.desktop']),
      ('bin/',['maths-tutor'])]
      )
# sudo python3 setup.py install --install-data=/usr
