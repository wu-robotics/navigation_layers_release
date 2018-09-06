Name:           ros-melodic-social-navigation-layers
Version:        0.4.2
Release:        0%{?dist}
Summary:        ROS social_navigation_layers package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/social_navigation_layers
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-angles
Requires:       ros-melodic-costmap-2d
Requires:       ros-melodic-dynamic-reconfigure
Requires:       ros-melodic-people-msgs
Requires:       ros-melodic-pluginlib
Requires:       ros-melodic-roscpp
BuildRequires:  ros-melodic-angles
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-costmap-2d
BuildRequires:  ros-melodic-dynamic-reconfigure
BuildRequires:  ros-melodic-people-msgs
BuildRequires:  ros-melodic-pluginlib
BuildRequires:  ros-melodic-roscpp

%description
Plugin-based layers for the navigation stack that implement various social
navigation contraints, like proxemic distance.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Sep 06 2018 David V. Lu!! <davidvlu@gmail.com> - 0.4.2-0
- Autogenerated by Bloom

* Fri Aug 31 2018 David V. Lu!! <davidvlu@gmail.com> - 0.4.0-0
- Autogenerated by Bloom

