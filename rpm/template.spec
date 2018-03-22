Name:           ros-melodic-tf2-sensor-msgs
Version:        0.5.17
Release:        1%{?dist}
Summary:        ROS tf2_sensor_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/tf2_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-melodic-python-orocos-kdl
Requires:       ros-melodic-rospy
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-tf2
Requires:       ros-melodic-tf2-ros
BuildRequires:  eigen3-devel
BuildRequires:  ros-melodic-catkin >= 0.5.6
BuildRequires:  ros-melodic-cmake-modules
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-tf2
BuildRequires:  ros-melodic-tf2-ros

%description
Small lib to transform sensor_msgs with tf. Most notably, PointCloud2

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
* Wed Mar 21 2018 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.17-1
- Autogenerated by Bloom

* Wed Mar 21 2018 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.5.17-0
- Autogenerated by Bloom

