Name:           ros-jade-rosconsole-bridge
Version:        0.4.4
Release:        0%{?dist}
Summary:        ROS rosconsole_bridge package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/rosconsole_bridge
Source0:        %{name}-%{version}.tar.gz

Requires:       console-bridge-devel
Requires:       ros-jade-rosconsole
BuildRequires:  console-bridge-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-rosconsole >= 1.11.5

%description
rosconsole_bridge is a package used in conjunction with console_bridge and
rosconsole for connecting console_bridge-based logging to rosconsole-based
logging.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon Apr 18 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.4-0
- Autogenerated by Bloom

* Fri Dec 26 2014 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.2-0
- Autogenerated by Bloom

